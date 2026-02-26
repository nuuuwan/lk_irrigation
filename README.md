# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_11:08:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 11:08:23 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:07:51 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-26 11:06:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.057 |  |
| 2026-02-26 11:05:22 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:05:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:05:04 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.029 |  |
| 2026-02-26 11:04:58 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:04:16 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:04:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:36 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 11:03:30 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:17 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:10 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-02-26 11:02:56 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:53 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:02:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:44 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:41 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:34 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-02-26 11:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:21 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:20 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-02-26 11:01:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:44 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-02-26 11:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:31 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 11:01:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:28 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:00:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:00:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 10:28:35 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.018 |  |
| 2026-02-26 10:20:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 10:15:03 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 11:02:34 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-02-26 11:01:31 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 11:03:36 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 11:02:44 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 10:03:01 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:28 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:41 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:21 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:17 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:56 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:07:51 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:05:22 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:30 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:02:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:05:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:04:16 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:03:10 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 11:04:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 10:15:03 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.008 |  |
| 2026-02-26 11:08:23 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:00:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:00:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:02:53 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:02:20 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-26 11:01:44 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-02-26 10:09:15 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-02-26 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-26 10:05:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-02-26 11:05:04 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.029 |  |
| 2026-02-26 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-02-26 11:03:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-02-26 11:06:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)