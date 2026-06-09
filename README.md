# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_17:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 17:12:05 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 17:10:19 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-06-09 17:08:41 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:08:34 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-06-09 17:07:47 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.356 |  |
| 2026-06-09 17:07:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:06:48 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:06:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 17:06:06 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.356 |  |
| 2026-06-09 17:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.039 |  |
| 2026-06-09 17:04:59 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:04:38 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-09 17:04:27 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 17:04:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-09 17:03:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-09 17:03:18 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-06-09 17:03:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:02:58 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:35 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:34 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-06-09 17:02:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:32 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:30 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-06-09 17:02:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:27 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:02:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:12 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:10 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-09 17:01:52 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:01:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-06-09 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 17:01:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:01:14 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.020 |  |
| 2026-06-09 17:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:00:29 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 16:26:23 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 17:02:10 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-09 17:04:27 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 17:03:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-09 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 17:06:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 17:12:05 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-09 17:04:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:01:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:12 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:58 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 15:05:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:01:52 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:04:59 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:32 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:07:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:18 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:00:29 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:02:35 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 17:03:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-09 17:08:41 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:06:48 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:02:27 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:03:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 17:08:34 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-06-09 17:10:19 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-06-09 17:04:38 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-09 17:01:14 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.020 |  |
| 2026-06-09 17:01:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-06-09 17:02:30 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-06-09 17:02:34 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-06-09 17:03:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-06-09 16:05:21 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.030 |  |
| 2026-06-09 17:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.039 |  |
| 2026-06-09 17:07:47 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.356 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)