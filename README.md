# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_10:17:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 10:17:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.025 |  |
| 2026-02-21 10:14:56 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:14:54 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-21 10:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.051 |  |
| 2026-02-21 10:09:11 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:08:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:08:12 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:07:42 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 10:07:41 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 10:07:22 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:06:19 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:05:25 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:05:23 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:03:35 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:03:35 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:03:26 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 10:03:26 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:03:26 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:39 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 10:02:22 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:02:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:02:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:14 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:02:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:11 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:05 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.075 |  |
| 2026-02-21 10:01:54 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.098 |  |
| 2026-02-21 10:01:53 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:01:51 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:48 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.031 |  |
| 2026-02-21 10:01:43 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.142 |  |
| 2026-02-21 10:01:41 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:33 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:19 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:01:18 | Padiyathalawa (Maduru Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-02-21 10:01:06 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:04 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:00:41 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 10:07:42 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 10:00:41 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-21 10:03:26 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 10:14:54 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-21 10:02:39 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 10:01:19 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:02:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:05:25 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:08:12 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 10:01:06 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:51 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:11 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:03:35 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:09:11 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:06:19 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:03:26 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:01:33 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:14:56 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:07:22 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-21 10:02:22 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:01:04 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:03:35 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:03:26 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-21 10:05:23 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:01:53 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:08:47 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:02:14 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-21 10:01:18 | Padiyathalawa (Maduru Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-02-21 10:17:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.025 |  |
| 2026-02-21 10:01:48 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.031 |  |
| 2026-02-21 10:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.051 |  |
| 2026-02-21 10:02:05 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.075 |  |
| 2026-02-21 10:01:54 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.098 |  |
| 2026-02-21 10:01:43 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)