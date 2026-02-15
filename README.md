# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_16:39:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,859 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 16:39:01 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:24:28 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:14:21 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-15 16:10:45 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.045 |  |
| 2026-02-15 16:09:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:07:53 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:07:18 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-02-15 16:07:14 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:06:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:06:55 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:05:59 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.204 |  |
| 2026-02-15 16:05:33 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:04:44 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.039 |  |
| 2026-02-15 16:04:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:04:21 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:04:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:03:27 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:17 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:58 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:53 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.050 |  |
| 2026-02-15 16:02:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:20 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:01:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:49 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:43 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:01:36 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:32 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:01:31 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:01:04 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.049 |  |
| 2026-02-15 16:00:54 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-02-15 16:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:00:50 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:00:40 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.030 |  |
| 2026-02-15 16:00:17 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:00:11 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 16:14:21 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-15 16:02:53 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:00:50 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:24:28 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:49 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:20 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:36 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:27 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:02:58 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:09:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:06:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:05:33 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:07:14 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:04:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:17 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:39:01 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:06:55 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:07:53 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:01:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:00:17 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 16:03:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:01:43 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:00:11 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-15 16:01:32 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:01:31 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:04:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-02-15 16:00:54 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-02-15 16:07:18 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-02-15 16:00:40 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.030 |  |
| 2026-02-15 16:04:44 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.039 |  |
| 2026-02-15 16:10:45 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.045 |  |
| 2026-02-15 16:01:04 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.049 |  |
| 2026-02-15 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.050 |  |
| 2026-02-15 16:05:59 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)