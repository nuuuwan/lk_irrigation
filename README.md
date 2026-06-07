# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_05:30:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,604 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 05:30:59 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.035 |  |
| 2026-06-07 05:25:32 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:19:15 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-07 05:17:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 05:16:18 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:12:06 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.250 |  |
| 2026-06-07 05:10:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 05:10:13 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-07 05:07:37 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 05:07:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:06:50 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-07 05:06:43 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-06-07 05:05:52 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-06-07 05:05:51 | Nawalapitiya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.516 | 🔺 Rising |
| 2026-06-07 05:05:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 05:05:20 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 05:05:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:56 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:24 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:17 | Ellagawa (Kalu Ganga) | 7.01 | 🟢 Normal | -0.010 |  |
| 2026-06-07 05:03:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:14 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:02:51 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 05:02:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:02:45 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:02:28 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 05:02:11 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-06-07 05:01:47 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-07 05:01:29 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:10 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:08 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:48:34 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-07 04:46:58 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:45:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 05:05:51 | Nawalapitiya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.516 | 🔺 Rising |
| 2026-06-07 05:10:13 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-07 05:02:11 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-06-07 05:01:47 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-07 05:05:52 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-06-07 05:06:50 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-07 05:17:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 05:10:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 05:05:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 05:02:28 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 05:05:20 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 05:19:15 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-07 05:07:37 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:29 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:05:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:16:18 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:56 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:04:24 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:10 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:02:45 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:07:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:05:09 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:01:08 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:25:32 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 05:03:17 | Ellagawa (Kalu Ganga) | 7.01 | 🟢 Normal | -0.010 |  |
| 2026-06-07 05:02:51 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 05:06:43 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-06-07 05:30:59 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.035 |  |
| 2026-06-07 05:12:06 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)