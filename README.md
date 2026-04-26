# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_19:34:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,807 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 19:34:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:21:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 19:17:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:14:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:11:23 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-26 19:10:10 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.056 |  |
| 2026-04-26 19:07:45 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-26 19:07:33 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-04-26 19:07:29 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:06:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:06:10 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:05:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-26 19:05:30 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:05:29 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-26 19:04:55 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |
| 2026-04-26 19:04:46 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-26 19:04:38 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:04:20 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-26 19:04:19 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-26 19:03:39 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:32 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:17 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-26 19:03:17 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:09 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:02:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-04-26 19:02:30 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 19:02:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-04-26 19:02:13 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:01:51 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:01:29 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:01:28 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-04-26 19:01:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:00:52 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:00:47 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:00:23 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.042 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 19:02:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-04-26 19:07:45 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-26 19:04:20 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-26 19:05:29 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-26 19:03:17 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-26 19:00:23 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-26 19:21:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 19:02:30 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 19:05:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-26 19:04:19 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-26 19:11:23 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:00:47 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:02:13 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:07:29 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:34:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:04:38 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:17:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:01:51 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:32 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:09 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:05:30 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:39 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:06:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:14:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 19:03:17 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 19:06:10 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:00:52 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:01:29 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:01:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-26 19:07:33 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-04-26 19:04:46 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-26 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-26 19:01:28 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-04-26 19:02:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-04-26 19:10:10 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.056 |  |
| 2026-04-26 19:04:55 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)