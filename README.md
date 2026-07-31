# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_15:10:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 15:10:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:09:05 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 15:07:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:07:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:07:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-31 15:06:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:38 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-31 15:06:09 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:04 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-31 15:06:02 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:05:51 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:05:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:05:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-31 15:05:28 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-31 15:04:48 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:04:04 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-07-31 15:03:57 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:03:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-31 15:03:07 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:03:02 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-31 15:02:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 15:02:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 15:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:22 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-31 15:02:08 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.075 |  |
| 2026-07-31 15:02:07 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:01:59 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 15:01:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 15:07:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-31 15:04:04 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-07-31 15:03:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-31 14:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-31 15:05:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-31 15:06:38 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-31 15:00:43 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-31 14:09:28 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 15:02:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 15:02:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 15:01:59 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 15:09:05 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 15:02:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-31 15:07:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:03:57 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:03:07 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:00:26 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:05:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:00:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:22 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:05:51 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:05:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:09 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:07 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:00:33 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:02:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:07:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:01:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:00:17 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:10:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:02 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:04:48 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 15:06:04 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-31 15:03:02 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-31 15:05:28 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-31 15:02:08 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)