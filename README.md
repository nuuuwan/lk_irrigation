# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_01:09:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,495 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 01:09:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:08:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:08:56 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 5.400 | 🔺 Rising |
| 2026-04-13 01:08:16 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | 5.400 | 🔺 Rising |
| 2026-04-13 01:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:07:10 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 01:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:06:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-13 01:06:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:06:09 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 01:05:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:05:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:05:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:05:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-04-13 01:04:10 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-13 01:04:01 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-13 01:03:36 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:03:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.132 |  |
| 2026-04-13 01:03:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:02:30 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 01:02:29 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:02:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:01:56 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 01:01:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:01:05 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-04-13 01:00:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.842 | 🔺 Rising |
| 2026-04-13 00:49:51 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-13 00:27:19 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 01:08:56 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 5.400 | 🔺 Rising |
| 2026-04-13 01:00:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.842 | 🔺 Rising |
| 2026-04-13 01:01:05 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-04-13 00:06:48 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-04-13 01:05:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-04-13 01:04:01 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-12 23:09:31 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 00:02:28 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-13 01:04:10 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-13 01:06:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-13 01:01:56 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 01:02:30 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 01:07:10 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 01:06:09 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 01:01:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:05:04 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:05:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 23:11:59 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:03:32 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:03:36 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:01:36 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:03:41 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:02:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:09:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:02:29 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:02:33 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:06:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:08:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:16:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:03:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-13 01:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:07:45 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-04-13 00:04:59 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-13 00:10:01 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.035 |  |
| 2026-04-12 21:19:02 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-04-13 01:03:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)