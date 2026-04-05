# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_05:21:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 05:21:52 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.038 |  |
| 2026-04-05 05:21:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:18:49 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2026-04-05 05:14:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.068 |  |
| 2026-04-05 05:13:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-05 05:10:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:09:52 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-05 05:08:23 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 05:08:17 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-04-05 05:08:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:07:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:07:09 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -7.712 |  |
| 2026-04-05 05:05:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-05 05:04:56 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.057 |  |
| 2026-04-05 05:04:47 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:04:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 05:04:28 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 05:03:59 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 05:03:10 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-04-05 05:02:41 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 05:02:33 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:02:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:02:07 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.049 |  |
| 2026-04-05 05:02:05 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-04-05 05:01:49 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:01:23 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 05:01:19 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-04-05 05:01:17 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-05 05:01:09 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-04-05 05:00:55 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-05 05:00:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:00:27 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 04:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-05 05:03:59 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 05:00:55 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-05 05:09:52 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-05 05:02:41 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 05:04:28 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 05:08:23 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 05:01:23 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 05:00:27 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 05:04:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 05:01:17 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-05 05:07:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:10:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:21:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:01:49 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:32 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:08:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:02:05 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-04-05 05:04:47 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:00:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:02:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:02:33 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:01:09 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-05 05:01:19 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-04-05 05:18:49 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2026-04-05 04:03:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-05 05:13:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 05:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-04-05 05:21:52 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.038 |  |
| 2026-04-05 05:05:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-05 05:02:07 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.049 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 05:04:56 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.057 |  |
| 2026-04-05 05:14:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.068 |  |
| 2026-04-05 05:08:17 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-04-05 05:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-04-05 05:07:09 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -7.712 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)