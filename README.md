# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_14:40:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 14:40:04 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:31:55 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:15:01 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:13:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:10:38 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:10:03 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-12 14:08:42 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.047 |  |
| 2026-07-12 14:08:09 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:08:03 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:07:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:07:45 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-12 14:06:21 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 14:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-12 14:03:33 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-12 14:03:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-12 14:04:08 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 14:10:03 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-12 14:01:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:02:38 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:02:17 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:02:10 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:03:45 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:00:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:03:32 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 13:01:58 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:13:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:15:01 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:01:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:07:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:02:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:40:04 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:08:09 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:01:44 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:06:21 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:07:45 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:31:55 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:03:42 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:10:38 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:08:03 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:02:58 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:00:55 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-07-12 14:04:13 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-07-12 14:03:13 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-07-12 14:04:56 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | -0.020 |  |
| 2026-07-12 14:01:41 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-12 14:00:54 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.022 |  |
| 2026-07-12 14:04:58 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-07-12 14:03:43 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-07-12 14:08:42 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.047 |  |
| 2026-07-12 14:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)