# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_00:28:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 00:28:35 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:22:01 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.008 |  |
| 2026-04-30 00:14:16 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:14:14 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:13:05 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:12:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:11:34 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:11:26 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:10:16 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-30 00:10:05 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:08:41 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:07:47 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-30 00:07:46 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:06:05 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-04-30 00:05:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.085 |  |
| 2026-04-30 00:05:24 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 00:05:07 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-04-30 00:05:03 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:04:05 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-30 00:04:04 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:03:51 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:03:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:03:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:03:14 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-30 00:03:01 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:45 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-30 00:02:39 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:11 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 00:01:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:01:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:00:11 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.031 |  |
| 2026-04-30 00:00:09 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 00:02:45 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-30 00:10:16 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-30 00:05:24 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 00:02:11 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 00:01:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:08:41 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:01:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:39 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:03:01 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:09:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:14:16 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:12:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:28:35 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:11:47 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:04:04 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:07:46 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:04:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:03:51 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:11:26 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:05:03 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:02:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-04-30 00:22:01 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.008 |  |
| 2026-04-30 00:11:34 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:13:05 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:03:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-04-30 00:07:47 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-30 00:04:05 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-30 00:06:05 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-04-30 00:00:09 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-04-30 00:03:14 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-30 00:00:11 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.031 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 00:05:07 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-04-30 00:05:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)