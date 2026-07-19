# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_04:25:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 04:25:51 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-20 04:24:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:16:56 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-07-20 04:11:34 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:08:28 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -48.000 |  |
| 2026-07-20 04:08:25 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -48.000 |  |
| 2026-07-20 04:08:23 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -48.000 |  |
| 2026-07-20 04:08:02 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-20 04:07:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-07-20 04:07:34 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:07:30 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:06:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.003 |  |
| 2026-07-20 04:05:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:07 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:04:23 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-07-20 04:04:17 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-20 04:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-20 04:03:21 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.050 |  |
| 2026-07-20 04:03:02 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:34 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:02:25 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:02:23 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:13 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.147 |  |
| 2026-07-20 04:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 04:01:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:01:39 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 04:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:00:58 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:00:45 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:00:36 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 03:54:58 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 04:07:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-07-20 04:04:23 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-07-20 04:08:02 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-20 04:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-20 04:25:51 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-20 04:04:17 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-20 04:01:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 04:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 04:00:36 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:07:34 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:02:34 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:05:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.003 |  |
| 2026-07-19 23:01:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:00:58 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:39 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:11:34 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:39 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 21:20:26 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:06:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-20 03:04:09 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:24:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 03:00:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:00:45 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:03:02 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:07 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:07:30 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:23 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:02:25 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:16:56 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-07-19 18:03:00 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.019 |  |
| 2026-07-20 04:03:21 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.050 |  |
| 2026-07-20 04:02:13 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.147 |  |
| 2026-07-20 04:08:28 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -48.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)