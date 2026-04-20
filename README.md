# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_19:00:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 19:00:40 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:11 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-04-20 19:00:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:57:29 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 18:22:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:16:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 18:13:41 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:12:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 18:09:31 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-04-20 18:08:44 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 19:00:11 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-04-20 18:07:28 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-20 18:08:44 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 18:03:01 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-20 18:03:39 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-20 18:02:24 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-20 18:01:49 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-20 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-20 18:57:29 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 18:02:57 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 18:03:53 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 18:16:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 18:03:59 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 18:02:56 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 18:02:30 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 18:05:42 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 18:00:24 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:04:01 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:22:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:40 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:03:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:00:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:13:41 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:04:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:05:50 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:31 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:05:00 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:02:24 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:09:31 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-04-20 18:03:47 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-04-20 18:03:19 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.026 |  |
| 2026-04-20 18:04:41 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.030 |  |
| 2026-04-20 18:00:40 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-04-20 18:03:21 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)