# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_07:00:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 07:00:06 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 06:34:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.001 |  |
| 2026-01-18 06:28:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:24:48 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:11:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:10:26 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:08:15 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.098 |  |
| 2026-01-18 06:07:59 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-01-18 06:07:47 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-18 06:07:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.294 |  |
| 2026-01-18 06:07:26 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:05:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-18 06:05:48 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-18 06:05:36 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 06:05:27 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:05:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 06:04:55 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 06:04:49 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:48 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:20 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:01 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 06:03:43 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 06:03:41 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-01-18 06:03:06 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 06:07:47 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-18 06:05:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-18 06:04:55 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 06:05:48 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-18 07:00:06 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 06:03:43 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 06:02:29 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 06:05:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 06:02:12 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.002 |  |
| 2026-01-18 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:01:17 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:00:52 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:02:56 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:02:33 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:07:26 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:49 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:10:26 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:20 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:28:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:01:44 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:02:56 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:00:35 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:01:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:11:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:04:48 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:24:48 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:01:32 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:05:27 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 06:34:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.001 |  |
| 2026-01-18 06:05:36 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 06:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-18 06:03:41 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-18 06:07:59 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-01-18 06:01:17 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.033 |  |
| 2026-01-18 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-01-18 06:01:34 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.084 |  |
| 2026-01-18 06:08:15 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.098 |  |
| 2026-01-18 06:07:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.294 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)