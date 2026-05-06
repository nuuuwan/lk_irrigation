# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_05:01:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 05:01:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:52 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.066 |  |
| 2026-05-07 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-07 05:01:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-07 05:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 05:01:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-07 05:01:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-07 05:00:53 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 05:00:44 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.093 |  |
| 2026-05-07 05:00:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:26:13 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-05-07 04:24:15 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-05-07 04:24:13 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-05-07 04:18:17 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-07 04:16:27 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.066 |  |
| 2026-05-07 04:14:30 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-07 04:12:27 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 04:24:15 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-05-07 04:03:07 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-05-07 03:05:51 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-07 04:02:30 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-05-07 04:03:13 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-07 04:05:35 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-07 05:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 04:01:17 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 04:01:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 01:01:19 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-07 04:09:17 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 05:01:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-07 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 05:01:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:01:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 04:04:41 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 04:14:30 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-07 05:00:53 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 04:18:17 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-07 05:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:03:43 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:00:58 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:00:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 04:01:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-07 04:02:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-07 05:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-07 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-07 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-07 05:01:52 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.066 |  |
| 2026-05-07 05:00:44 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.093 |  |
| 2026-05-07 04:02:09 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.146 |  |
| 2026-05-07 03:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -2.082 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)