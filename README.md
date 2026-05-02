# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_10:33:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 10:33:46 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-02 10:31:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:22:43 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:20:50 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:14:24 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 10:13:14 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:11:32 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-05-02 10:10:11 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-02 10:07:53 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.018 |  |
| 2026-05-02 10:07:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 10:07:00 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:06:48 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:05:45 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:05:35 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-02 10:05:15 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:04:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:03:48 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 10:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:03:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-05-02 10:03:29 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-02 10:03:22 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-02 10:03:19 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:03:11 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.061 |  |
| 2026-05-02 10:02:59 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.112 |  |
| 2026-05-02 10:02:59 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-02 10:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-05-02 10:02:21 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-05-02 10:02:18 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:54 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:34 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-05-02 10:01:32 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2026-05-02 10:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:00:45 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:00:44 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-05-02 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 09:59:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-02 10:05:35 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-02 10:03:29 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-02 10:14:24 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 10:03:48 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 10:07:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 10:33:46 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-02 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:31:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:00:45 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:22:43 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:02:18 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:13:14 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:07:00 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:04:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:05:15 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:05:45 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:54 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:06:48 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-02 10:10:11 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-02 10:11:32 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-05-02 10:20:50 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:03:19 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:03:22 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-02 09:59:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-02 10:00:44 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-05-02 10:07:53 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.018 |  |
| 2026-05-02 10:01:32 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2026-05-02 10:02:59 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-02 10:03:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-05-02 10:02:21 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-05-02 10:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-05-02 10:01:34 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-05-02 10:03:11 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.061 |  |
| 2026-05-02 09:00:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-05-02 10:02:59 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)