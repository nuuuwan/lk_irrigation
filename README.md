# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_08:08:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 08:08:52 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-04-23 08:08:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-04-23 08:08:06 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.039 |  |
| 2026-04-23 08:07:40 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-23 08:06:47 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:06:15 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:06:06 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-04-23 08:06:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-23 08:05:16 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:05:12 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.042 |  |
| 2026-04-23 08:05:03 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:04:57 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 08:04:26 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 08:03:47 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.021 |  |
| 2026-04-23 08:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-23 08:03:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-04-23 08:03:16 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 08:03:16 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-23 08:03:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:02:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 08:02:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.054 |  |
| 2026-04-23 08:02:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.122 |  |
| 2026-04-23 08:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:02:08 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:01:37 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-04-23 08:01:35 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:01:29 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-23 08:01:28 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 08:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-04-23 08:01:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.162 |  |
| 2026-04-23 08:01:03 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:01:03 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.035 |  |
| 2026-04-23 08:00:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:00:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-23 08:00:33 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.156 |  |
| 2026-04-23 08:00:17 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-04-23 07:19:34 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-23 07:18:19 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 07:02:23 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-23 08:03:16 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-23 08:06:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-23 08:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-23 08:01:29 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-23 07:05:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 08:04:26 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 08:07:40 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-23 08:03:16 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 08:02:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 08:01:28 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 08:04:57 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 08:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:00:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:05:16 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:05:03 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:02:08 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:06:15 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:08:52 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-04-23 07:00:40 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 08:08:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-04-23 08:06:47 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:01:35 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:03:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-23 08:03:47 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.021 |  |
| 2026-04-23 08:03:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-04-23 07:18:19 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.025 |  |
| 2026-04-23 08:06:06 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-04-23 08:00:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-23 08:00:17 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-04-23 08:01:03 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.035 |  |
| 2026-04-23 08:08:06 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.039 |  |
| 2026-04-23 08:01:37 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-04-23 08:05:12 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.042 |  |
| 2026-04-23 08:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-04-23 08:02:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.054 |  |
| 2026-04-23 08:02:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.122 |  |
| 2026-04-23 08:00:33 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.156 |  |
| 2026-04-23 08:01:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)