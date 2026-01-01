# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_17:28:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,886 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 17:28:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.042 |  |
| 2026-01-01 17:24:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-01 17:15:54 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.008 |  |
| 2026-01-01 17:13:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:31 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 17:07:46 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:07:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:06:59 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:06:58 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-01 17:06:56 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-01 17:06:18 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:06:16 | Katharagama (Menik Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-01 17:06:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 17:05:43 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-01-01 17:05:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-01-01 17:04:44 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:04:13 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 17:03:42 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:03:34 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.069 |  |
| 2026-01-01 17:03:20 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:03:01 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:02:54 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:02:44 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 17:02:41 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:02:33 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:02:28 | Horowpothana (Yan Oya) | 3.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-01 17:02:14 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.082 |  |
| 2026-01-01 17:02:14 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.072 |  |
| 2026-01-01 17:02:14 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:02:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-01-01 17:02:10 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.049 |  |
| 2026-01-01 17:02:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:01:51 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:00:36 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:00:35 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:00:34 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | -0.032 |  |
| 2026-01-01 17:00:10 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:45:22 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 17:06:58 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-01 17:06:16 | Katharagama (Menik Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-01 17:02:28 | Horowpothana (Yan Oya) | 3.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-01 17:02:44 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 17:04:13 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 17:06:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 17:09:31 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 17:02:33 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:00:10 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:03:01 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:03:42 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:04:44 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:02:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:01:51 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:13:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:15:54 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.008 |  |
| 2026-01-01 17:07:46 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:02:54 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:02:14 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:06:18 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:00:35 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:03:20 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:06:59 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 17:24:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-01 16:05:40 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-01-01 17:02:41 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:02:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:00:36 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-01-01 17:05:43 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-01-01 17:05:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-01-01 17:00:34 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | -0.032 |  |
| 2026-01-01 17:28:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.042 |  |
| 2026-01-01 17:02:10 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.049 |  |
| 2026-01-01 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-01-01 17:03:34 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.069 |  |
| 2026-01-01 17:02:14 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.072 |  |
| 2026-01-01 17:02:14 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)