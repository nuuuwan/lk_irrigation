# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_23:09:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,868 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 23:09:33 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-27 23:07:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:07:11 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:06:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:06:11 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:05:39 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:05:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:04:05 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:54 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:40 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.058 |  |
| 2026-02-27 23:03:01 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:46 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-27 23:02:43 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:28 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 23:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 23:02:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:04 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:53 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:52 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-27 23:01:21 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.012 |  |
| 2026-02-27 23:01:19 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-02-27 23:01:19 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:41 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:38 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:36 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:32 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:19 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 22:41:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 22:30:40 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 23:02:46 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-27 23:09:33 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-27 23:02:28 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 22:04:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-27 23:00:19 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 22:14:14 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-27 23:02:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 23:06:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:52 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:04:05 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:41 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:05:39 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 22:03:26 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:43 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:05:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:07:11 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:01 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:54 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:03:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:06:11 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:19 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:00:32 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:07:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:02:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-27 23:01:53 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-27 22:03:11 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-02-27 23:01:21 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.012 |  |
| 2026-02-27 23:01:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-27 23:01:19 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-27 23:03:40 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.058 |  |
| 2026-02-27 22:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.087 |  |
| 2026-02-27 22:02:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)