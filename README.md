# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_19:25:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 19:25:08 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-07 19:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-07-07 19:11:12 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:10:39 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:10:13 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:07:52 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:07:00 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:06:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:06:20 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.046 |  |
| 2026-07-07 19:05:41 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 19:05:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-07-07 19:05:17 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-07 19:05:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:05:00 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:55 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:22 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-07 19:04:05 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:03:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 19:03:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:03:54 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:03:34 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:03:05 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:02:39 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-07 19:02:31 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:18 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-07 19:02:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:14 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.038 |  |
| 2026-07-07 19:02:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:01:12 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.042 |  |
| 2026-07-07 19:01:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:00:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 19:04:22 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-07 19:02:18 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-07 19:03:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-07 19:05:17 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-07 19:05:41 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 19:25:08 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:00:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:05:00 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:31 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:03:34 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:01:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:10:13 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:07:52 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:11:12 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:03:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:14 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:55 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:10:39 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:05:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:02:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:04:05 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 19:05:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-07-07 19:03:05 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:03:54 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:07:00 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-07 19:02:39 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-07 19:02:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.038 |  |
| 2026-07-07 19:01:12 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.042 |  |
| 2026-07-07 19:06:20 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.046 |  |
| 2026-07-07 19:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)