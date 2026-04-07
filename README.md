# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_11:18:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 11:18:50 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:15:42 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:12:08 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:10:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:08:48 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-04-07 11:08:26 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:08:17 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:08:07 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:07:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 11:07:01 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-07 11:06:26 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:06:09 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.068 |  |
| 2026-04-07 11:06:08 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:05:26 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:05:21 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-04-07 11:05:01 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.056 |  |
| 2026-04-07 11:04:32 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:04:22 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-07 11:04:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-04-07 11:03:59 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:03:57 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.019 |  |
| 2026-04-07 11:03:34 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:03:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-04-07 11:03:11 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:03:05 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:02:55 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-07 11:02:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-04-07 11:02:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:02:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.041 |  |
| 2026-04-07 11:02:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-04-07 11:01:57 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-07 11:01:51 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-04-07 11:01:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:01:35 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.189 |  |
| 2026-04-07 11:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:00:29 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:00:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.033 |  |
| 2026-04-07 11:00:08 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 11:02:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-04-07 11:07:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 11:04:22 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-07 11:08:17 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:00:08 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:03:11 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:02:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:01:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:15:42 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:18:50 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:03:34 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:02:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:10:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:06:26 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:08:26 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:12:08 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-07 11:08:07 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:04:32 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:06:08 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:03:05 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:00:29 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-04-07 11:02:55 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-07 11:04:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-04-07 11:03:57 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.019 |  |
| 2026-04-07 11:01:57 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-07 11:07:01 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-07 11:01:51 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-04-07 11:05:21 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-04-07 11:00:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.033 |  |
| 2026-04-07 11:03:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-04-07 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-04-07 11:02:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.041 |  |
| 2026-04-07 11:08:48 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-04-07 11:05:01 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.056 |  |
| 2026-04-07 11:06:09 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.068 |  |
| 2026-04-07 11:01:35 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)