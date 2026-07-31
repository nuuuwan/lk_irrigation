# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_20:00:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 20:00:33 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-31 19:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -17.673 |  |
| 2026-07-31 19:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -17.673 |  |
| 2026-07-31 19:14:33 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-31 19:13:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 19:02:58 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-07-31 19:03:05 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-31 19:08:26 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-31 19:04:10 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 19:01:09 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-31 19:04:23 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-31 19:05:52 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 19:04:32 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 19:05:52 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 19:14:33 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-31 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:02:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:02:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:01:32 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:01:53 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:04:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:05:52 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:03:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:03:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:01:58 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:02:14 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:09:47 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:07:23 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:13:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:08:06 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:01:49 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 19:04:24 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-31 19:06:00 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2026-07-31 19:05:47 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-31 20:00:33 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-31 19:01:17 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.034 |  |
| 2026-07-31 19:07:22 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.036 |  |
| 2026-07-31 19:07:42 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.045 |  |
| 2026-07-31 19:08:57 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.119 |  |
| 2026-07-31 19:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -17.673 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)