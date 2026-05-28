# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_21:09:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 21:09:28 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:08:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:08:02 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 21:07:26 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:07:23 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-28 21:07:19 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.107 |  |
| 2026-05-28 21:07:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:06:55 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | -0.010 |  |
| 2026-05-28 21:06:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-05-28 21:06:01 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-28 21:05:54 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.273 |  |
| 2026-05-28 21:05:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:05:25 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:04:57 | Pitabeddara (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-28 21:04:55 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:04:50 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:04:21 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.117 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 21:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-05-28 21:06:55 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | -0.010 |  |
| 2026-05-28 21:03:11 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-05-28 21:07:23 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-28 21:04:21 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-28 21:00:26 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-28 21:06:01 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-28 21:03:45 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-28 21:04:57 | Pitabeddara (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-28 21:01:09 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-28 21:02:46 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-28 21:03:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 21:02:51 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-28 21:08:02 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 21:02:43 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 21:01:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 21:02:00 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 21:01:31 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 21:05:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:02:07 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:04:50 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:03:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:09:28 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:07:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:02:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:06:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:08:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:04:55 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:05:25 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 21:01:37 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-05-28 21:02:00 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-28 21:02:29 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-28 21:02:31 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-05-28 21:07:19 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.107 |  |
| 2026-05-28 21:05:54 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)