# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_21:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 21:14:32 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.918 |  |
| 2026-05-07 21:11:12 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.064 |  |
| 2026-05-07 21:09:46 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-07 21:09:03 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-05-07 21:08:27 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-05-07 21:07:59 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.093 |  |
| 2026-05-07 21:07:32 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-05-07 21:07:31 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:06:27 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-05-07 21:05:54 | Thanamalwila (Kirindi Oya) | 2.90 | 🟢 Normal | -0.203 |  |
| 2026-05-07 21:05:40 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:05:37 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-05-07 21:05:32 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.052 |  |
| 2026-05-07 21:05:26 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.089 |  |
| 2026-05-07 21:05:22 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-07 21:05:20 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-05-07 21:05:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:04:24 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 1.120 | 🔺 Rising |
| 2026-05-07 21:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:03:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 21:03:32 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:03:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:03:20 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | 1.231 | 🔺 Rising |
| 2026-05-07 21:02:59 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.080 |  |
| 2026-05-07 21:02:58 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.023 |  |
| 2026-05-07 21:02:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-05-07 21:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.110 |  |
| 2026-05-07 21:02:34 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:02:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 21:02:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-07 21:01:58 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.713 |  |
| 2026-05-07 21:01:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 21:01:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:01:17 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:16 | Kuda Oya (Kirindi Oya) | 3.38 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 21:03:20 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | 1.231 | 🔺 Rising |
| 2026-05-07 21:04:24 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 1.120 | 🔺 Rising |
| 2026-05-07 21:05:20 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-05-07 21:06:27 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-05-07 21:02:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 21:05:37 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-05-07 21:09:46 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-07 21:05:22 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-07 21:02:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-07 21:03:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 21:01:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 21:01:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:03:32 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:05:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:05:40 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:03:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:07:31 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:17 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:02:58 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.023 |  |
| 2026-05-07 21:09:03 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-05-07 18:02:13 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.029 |  |
| 2026-05-07 21:07:32 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-05-07 21:08:27 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-05-07 21:05:32 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.052 |  |
| 2026-05-07 21:02:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-07 21:11:12 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.064 |  |
| 2026-05-07 21:02:59 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.080 |  |
| 2026-05-07 21:05:26 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.089 |  |
| 2026-05-07 21:07:59 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.093 |  |
| 2026-05-07 21:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.110 |  |
| 2026-05-07 21:01:16 | Kuda Oya (Kirindi Oya) | 3.38 | 🟢 Normal | -0.120 |  |
| 2026-05-07 21:05:54 | Thanamalwila (Kirindi Oya) | 2.90 | 🟢 Normal | -0.203 |  |
| 2026-05-07 21:01:58 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.713 |  |
| 2026-05-07 21:14:32 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.918 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)