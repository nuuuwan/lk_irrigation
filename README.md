# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_09:15:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,002 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 09:15:09 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:12:05 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:08:24 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-07-22 09:07:46 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:07:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-22 09:04:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.022 |  |
| 2026-07-22 09:04:42 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:04:27 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:04:25 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:04:16 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 09:03:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:03:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:03:27 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:03:22 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:55 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.012 |  |
| 2026-07-22 09:02:55 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:50 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:38 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-22 09:02:27 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-07-22 09:02:25 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:02:22 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 09:02:21 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-07-22 09:02:14 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:02:06 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:00 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:01:55 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.050 |  |
| 2026-07-22 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-22 09:01:37 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.300 |  |
| 2026-07-22 09:01:14 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-07-22 09:00:56 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:43 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:39 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 09:00:38 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:31 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:14 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-22 08:34:34 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 09:02:38 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-22 09:07:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-22 09:04:16 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 09:02:22 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-22 09:00:39 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 09:00:43 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:31 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:00 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:06 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:50 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:21 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:07:46 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:03:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 08:05:08 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:03:22 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:15:09 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:03:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:04:25 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:14 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:56 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:02:55 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:04:27 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:38 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:12:05 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:00:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-22 09:08:24 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-07-22 09:03:27 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:04:42 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:02:25 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:02:14 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-22 09:01:14 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-07-22 09:02:55 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.012 |  |
| 2026-07-22 09:04:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.022 |  |
| 2026-07-22 09:02:27 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-07-22 09:01:55 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.050 |  |
| 2026-07-22 09:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-07-22 09:01:37 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)