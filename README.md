# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_01:01:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 01:01:24 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:01:20 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.144 |  |
| 2026-07-31 01:01:02 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:30:40 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-07-31 00:16:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:16:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 00:05:02 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-07-31 00:16:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-31 00:05:00 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-31 00:03:34 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-31 00:05:23 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-31 00:04:53 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 00:06:03 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 00:05:17 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 00:05:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:02:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:09:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 22:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 23:24:53 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 23:02:31 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-30 23:03:18 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:03:12 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:01:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 23:01:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:01:02 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:01:24 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:03:48 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:16:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:01:20 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:03:52 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:04:02 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:02:08 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 00:03:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.005 |  |
| 2026-07-31 00:08:40 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-07-31 00:04:28 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-31 00:04:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-31 00:10:58 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.026 |  |
| 2026-07-31 00:12:27 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.045 |  |
| 2026-07-30 21:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-07-31 00:30:40 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |
| 2026-07-31 00:03:41 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.089 |  |
| 2026-07-31 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)