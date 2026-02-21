# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_13:08:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 13:08:58 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:08:29 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:08:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.018 |  |
| 2026-02-21 13:07:52 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.022 |  |
| 2026-02-21 13:06:45 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:06:22 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:05:20 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-02-21 13:05:02 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:04:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:04:38 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.083 |  |
| 2026-02-21 13:04:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.064 |  |
| 2026-02-21 13:04:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-02-21 13:04:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:03:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:03:19 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-21 13:02:58 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 13:02:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-21 13:02:51 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:41 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:26 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:19 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-21 13:02:03 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-02-21 13:01:52 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.060 |  |
| 2026-02-21 13:01:39 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:01:25 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:01:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-21 13:01:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-21 13:01:10 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 13:00:58 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.033 |  |
| 2026-02-21 13:00:53 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:41 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:41 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:24 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.090 |  |
| 2026-02-21 13:00:13 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:50:24 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 13:02:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-21 12:06:24 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-21 13:02:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-21 13:01:10 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 13:02:58 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 13:01:25 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:06:45 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:03:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:53 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:05:02 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:05:20 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:41 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:08:29 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:04:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:01:39 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:02:19 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:08:58 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:13 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:00:41 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:06:22 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:41 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:04:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:26 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:02:51 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-21 13:08:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.018 |  |
| 2026-02-21 13:01:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-21 13:02:03 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-02-21 13:07:52 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.022 |  |
| 2026-02-21 13:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-02-21 13:04:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-02-21 13:01:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-21 13:03:19 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-21 13:00:58 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.033 |  |
| 2026-02-21 13:01:52 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.060 |  |
| 2026-02-21 13:04:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.064 |  |
| 2026-02-21 13:04:38 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.083 |  |
| 2026-02-21 13:00:24 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)