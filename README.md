# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_06:31:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,263 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 06:31:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:16:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.078 |  |
| 2026-04-17 06:10:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.108 |  |
| 2026-04-17 06:09:39 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-04-17 06:08:56 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-17 06:08:46 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:08:35 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.068 |  |
| 2026-04-17 06:08:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:08:19 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-17 06:06:56 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:06:30 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.038 |  |
| 2026-04-17 06:05:53 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.056 |  |
| 2026-04-17 06:05:38 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:04:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:04:19 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.029 |  |
| 2026-04-17 06:04:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:04:16 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-17 06:04:01 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:03:33 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.083 |  |
| 2026-04-17 06:03:16 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 06:03:07 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 06:03:05 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:02:57 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.153 |  |
| 2026-04-17 06:02:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:02:30 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-04-17 06:02:22 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:02:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 06:02:19 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-17 06:02:06 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:02:06 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 06:01:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:01:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:01:10 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:00:19 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 06:00:16 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-17 06:00:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.058 |  |
| 2026-04-17 05:59:47 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.068 |  |
| 2026-04-17 05:52:58 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 06:00:19 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 06:03:16 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 06:02:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 06:02:06 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 06:00:16 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-17 06:03:07 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 06:04:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:03:05 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:01:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:06:56 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:31:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:05:38 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:04:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:02:22 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:08:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:08:46 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:08:19 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-17 05:05:40 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-04-17 06:02:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:01:10 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:02:06 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:04:01 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:08:56 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-17 06:02:19 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-17 06:04:16 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-17 06:04:19 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.029 |  |
| 2026-04-17 06:09:39 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-04-17 06:06:30 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.038 |  |
| 2026-04-17 06:05:53 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.056 |  |
| 2026-04-17 06:00:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.058 |  |
| 2026-04-17 06:02:30 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-04-17 06:08:35 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.068 |  |
| 2026-04-17 06:16:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.078 |  |
| 2026-04-17 06:03:33 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.083 |  |
| 2026-04-17 06:10:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.108 |  |
| 2026-04-17 06:02:57 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)