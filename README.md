# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_09:35:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 09:35:12 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:23:30 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.007 |  |
| 2026-05-02 09:18:32 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-05-02 09:14:18 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:12:49 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:10:50 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-02 09:09:13 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.226 |  |
| 2026-05-02 09:07:27 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-02 09:07:03 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.054 |  |
| 2026-05-02 09:06:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:06:08 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-05-02 09:05:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-05-02 09:05:26 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:05:11 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 09:04:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:04:24 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.040 |  |
| 2026-05-02 09:04:11 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.079 |  |
| 2026-05-02 09:03:59 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:03:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:03:34 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:03:26 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:03:17 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:02:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:02:47 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.150 |  |
| 2026-05-02 09:02:40 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-02 09:02:40 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-02 09:02:32 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-05-02 09:02:32 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.030 |  |
| 2026-05-02 09:02:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.070 |  |
| 2026-05-02 09:02:04 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:01:56 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:54 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:01:41 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:12 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 09:01:06 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:00:47 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-02 09:00:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 09:00:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-05-02 08:54:47 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.150 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 09:02:40 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-02 09:00:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 09:01:12 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 09:05:11 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 09:06:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:41 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:56 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:01:06 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:02:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:14:18 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:35:12 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:02:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:04:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:03:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:03:34 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:23:30 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.007 |  |
| 2026-05-02 09:10:50 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-02 09:03:59 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:05:26 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:02:04 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:03:17 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:03:26 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:01:54 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:00:47 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-02 09:07:27 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-02 09:02:32 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-05-02 09:06:08 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-05-02 09:02:32 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.030 |  |
| 2026-05-02 09:02:40 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-02 09:04:24 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.040 |  |
| 2026-05-02 09:05:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-05-02 09:18:32 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-05-02 09:07:03 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.054 |  |
| 2026-05-02 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.070 |  |
| 2026-05-02 09:04:11 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.079 |  |
| 2026-05-02 09:00:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-05-02 09:02:47 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.150 |  |
| 2026-05-02 09:09:13 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)