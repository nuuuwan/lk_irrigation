# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_22:01:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 22:01:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-07-16 22:00:52 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.063 |  |
| 2026-07-16 22:00:30 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 22:00:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:24:27 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:21:51 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:16:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.053 |  |
| 2026-07-16 21:16:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.053 |  |
| 2026-07-16 21:12:44 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 21:06:52 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-07-16 21:03:47 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-16 18:01:19 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 22:00:30 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 21:02:44 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:01:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:24:27 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:02:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:01:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:01:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:09:00 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:06:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:21:51 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:03:24 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:06:24 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:07:41 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:00:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:04:36 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:03:19 | Moraketiya (Walawe Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:02:06 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:02:34 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:05:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:06:52 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:09:40 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:01:35 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:03:06 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:03:44 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:05:20 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:03:08 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:01:13 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-16 21:01:10 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.021 |  |
| 2026-07-16 21:01:45 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-07-16 21:05:12 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-07-16 21:04:54 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-07-16 21:04:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-07-16 22:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-07-16 22:00:52 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.063 |  |
| 2026-07-16 21:05:10 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)