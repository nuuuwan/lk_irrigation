# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_10:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 10:03:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-09 10:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-02-09 10:03:17 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 10:03:15 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 10:03:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-02-09 10:02:41 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-02-09 10:02:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:02:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-02-09 10:02:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:06 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.082 |  |
| 2026-02-09 10:01:57 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.020 |  |
| 2026-02-09 10:01:57 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-02-09 10:01:54 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:43 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:29 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:01:12 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:56 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:51 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:45 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:00:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:26:53 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:22:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-02-09 09:14:04 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-02-09 09:13:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-09 09:10:08 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:08:25 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 09:13:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-09 10:03:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-09 10:03:15 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 10:03:17 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 09:04:19 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-09 10:01:54 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:43 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:56 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:02:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:04:46 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:26:53 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:08:25 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 09:10:08 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:12 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:51 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 08:22:51 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-02-09 10:02:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-09 09:07:20 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:01:29 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-02-09 09:05:50 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:00:45 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-09 09:06:54 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-02-09 10:01:57 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.020 |  |
| 2026-02-09 10:02:41 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-02-09 09:14:04 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-02-09 10:03:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-02-09 10:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-02-09 10:01:57 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-02-09 09:06:34 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.074 |  |
| 2026-02-09 10:02:06 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.082 |  |
| 2026-02-09 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)