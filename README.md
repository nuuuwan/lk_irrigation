# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_17:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 17:03:18 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:39 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 17:02:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 17:02:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:17 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:15 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-01-25 17:02:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:02:07 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:03 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.023 |  |
| 2026-01-25 17:01:45 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.005 |  |
| 2026-01-25 17:01:43 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:35 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.040 |  |
| 2026-01-25 17:01:31 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 17:01:30 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:01:16 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:00:56 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 17:00:51 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:28:26 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:18:37 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:15:39 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-25 16:14:43 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:09:53 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.955 | 🔺 Rising |
| 2026-01-25 16:08:53 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -0.023 |  |
| 2026-01-25 16:07:16 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 16:09:53 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.955 | 🔺 Rising |
| 2026-01-25 16:01:10 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-25 16:01:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-25 16:15:39 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-25 17:00:56 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 17:01:31 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 17:02:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 17:02:39 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:03:52 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 17:02:07 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:17 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:43 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:06:15 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:14:43 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:03:18 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:28:26 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:04:04 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:26 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:30 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:18 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:04:03 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:06:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:02:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 17:01:45 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.005 |  |
| 2026-01-25 16:07:16 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:01:16 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:01:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:03:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:37 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:02:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:10 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:00:51 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-25 17:02:03 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.023 |  |
| 2026-01-25 17:02:15 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-01-25 16:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-25 17:01:35 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)