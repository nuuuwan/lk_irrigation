# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_10:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 10:11:50 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-23 10:09:52 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.035 |  |
| 2026-02-23 10:08:19 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:07:39 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.094 |  |
| 2026-02-23 10:07:38 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.029 |  |
| 2026-02-23 10:07:37 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-02-23 10:07:33 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-23 10:07:23 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-02-23 10:06:42 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:06:36 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-02-23 10:06:27 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:05:23 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:05:20 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:05:15 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-02-23 10:04:35 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 10:04:14 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.120 |  |
| 2026-02-23 10:04:03 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:03:47 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-02-23 10:03:26 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:03:26 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-23 10:03:25 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:03:09 | Manampitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-23 10:03:06 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-02-23 10:02:54 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:02:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:27 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.081 |  |
| 2026-02-23 10:02:26 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:02:23 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | -0.154 |  |
| 2026-02-23 10:02:22 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:19 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:17 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.101 |  |
| 2026-02-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.061 |  |
| 2026-02-23 10:01:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:40 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:22 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:59:26 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 10:03:26 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-23 10:03:09 | Manampitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-23 10:07:33 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-23 10:04:35 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 10:02:54 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:40 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:03:26 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:02:26 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:06:27 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:05:20 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:06:42 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:02:17 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:11:50 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-23 10:04:03 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:03:25 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:19 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:05:23 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:02:22 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:00:22 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:08:19 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:06:36 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-02-23 10:03:06 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-02-23 10:07:23 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-02-23 10:07:38 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.029 |  |
| 2026-02-23 10:07:37 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-02-23 10:09:52 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.035 |  |
| 2026-02-23 10:05:15 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-02-23 10:03:47 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-02-23 10:01:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.061 |  |
| 2026-02-23 10:02:27 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.081 |  |
| 2026-02-23 10:07:39 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.094 |  |
| 2026-02-23 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.101 |  |
| 2026-02-23 10:04:14 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.120 |  |
| 2026-02-23 10:02:23 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)