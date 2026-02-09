# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_10:30:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 10:30:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:22:41 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:18:45 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.037 |  |
| 2026-02-09 10:17:50 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:17:08 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-09 10:15:40 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:10:41 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-09 10:10:13 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 10:08:38 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:06:23 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:05:59 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:04:33 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.062 |  |
| 2026-02-09 10:04:30 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 10:03:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-09 10:17:08 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-09 10:03:15 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 10:03:17 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 10:10:13 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 10:01:54 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:43 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:56 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:04:30 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:05:59 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:08:38 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:22:41 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:15:40 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:17:50 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:03:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:12 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:06:23 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:30:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:00:51 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:02:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:01:29 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:00:45 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:10:41 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-09 10:01:57 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.020 |  |
| 2026-02-09 10:02:41 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-02-09 10:03:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-02-09 10:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-02-09 10:18:45 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.037 |  |
| 2026-02-09 10:04:33 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.062 |  |
| 2026-02-09 10:01:57 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-02-09 10:02:06 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.082 |  |
| 2026-02-09 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)