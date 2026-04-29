# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_20:00:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 20:00:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:58:36 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-29 19:16:10 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.008 |  |
| 2026-04-29 19:11:37 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-29 19:10:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 19:10:40 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-04-29 19:10:22 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 1.009 | 🔺 Rising |
| 2026-04-29 19:08:33 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:08:18 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 19:08:03 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-04-29 19:07:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 19:10:22 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 1.009 | 🔺 Rising |
| 2026-04-29 19:05:07 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-29 19:03:23 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-29 19:02:36 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 19:00:29 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 19:02:44 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-29 19:58:36 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-29 19:02:09 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 19:02:40 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 19:08:18 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 19:03:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 19:10:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 20:00:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:04:17 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:01:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:08:33 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:07:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:07:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:02:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:03:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:02:25 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:01:45 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:16:10 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.008 |  |
| 2026-04-29 19:10:40 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-04-29 19:08:03 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-04-29 19:05:27 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-29 19:05:26 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-29 19:00:57 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-29 19:04:44 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:02:19 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 19:06:46 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.019 |  |
| 2026-04-29 19:07:15 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-04-29 19:06:18 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.046 |  |
| 2026-04-29 19:02:04 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.049 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 19:02:30 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)