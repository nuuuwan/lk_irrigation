# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_19:22:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 19:22:59 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:22:09 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 19:19:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-06-26 19:12:07 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:08:35 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:08:24 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:07:33 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 19:06:04 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-26 19:06:02 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-26 19:05:53 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:05:51 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:05:26 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-06-26 19:05:23 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-26 19:05:21 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-06-26 19:05:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.010 |  |
| 2026-06-26 19:04:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-06-26 19:04:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:04:04 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.038 |  |
| 2026-06-26 19:04:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 19:03:58 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:03:51 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:03:19 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:03:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:57 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:02:44 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:02:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:26 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:01:25 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:19 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:09 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:00:41 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:00:29 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 19:05:23 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-26 19:06:02 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-26 19:06:04 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-26 19:22:09 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 19:04:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 19:02:44 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:01:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:03:19 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:04:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:05:51 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 19:07:33 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:57 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:25 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:03:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:08:35 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:26 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:03:58 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:19 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:08:24 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:02:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:00:41 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:03:51 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:22:59 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:01:09 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:12:07 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:19:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-06-26 19:05:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.010 |  |
| 2026-06-26 19:00:29 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-26 19:05:26 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.016 |  |
| 2026-06-26 19:05:21 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-06-26 19:04:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-06-26 19:04:04 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.038 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)