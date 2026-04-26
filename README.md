# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_17:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 17:14:33 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:14:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:13:32 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-26 17:12:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-26 17:10:13 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-26 17:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:09:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 17:08:33 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 17:08:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-26 17:07:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:07:24 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:06:30 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:05:41 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:05:35 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:05:09 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:04:54 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:04:50 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:04:30 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:04:16 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-26 17:03:51 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:03:28 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:02:33 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-04-26 17:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:02:10 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-04-26 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-04-26 17:02:04 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-26 17:01:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-26 17:01:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:53 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:01:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-26 17:01:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:21 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:11 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-26 17:00:40 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-04-26 17:00:34 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:00:33 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:00:33 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-26 17:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 17:01:11 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-26 17:04:16 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-26 17:13:32 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-26 17:10:13 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-26 17:01:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-26 17:00:33 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-26 17:08:33 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 17:09:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 16:14:45 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-26 17:08:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-26 17:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 17:00:34 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:05:09 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 16:06:00 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:04:50 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:05:35 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:00:33 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:14:33 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:07:24 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:06:30 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:14:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 17:01:21 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-26 16:14:45 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-04-26 17:05:41 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:03:28 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:01:53 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:04:30 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:03:51 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-26 17:12:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-26 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-04-26 17:02:04 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-26 17:01:29 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-26 17:00:40 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-04-26 17:02:10 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-04-26 17:02:33 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)