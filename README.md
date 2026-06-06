# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_14:14:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 14:14:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:13:27 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-06 14:12:20 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-06-06 14:12:12 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:09:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.038 |  |
| 2026-06-06 14:09:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:09:10 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:07:24 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 14:07:20 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 14:07:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:06:45 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:06:21 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:06:02 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:05:50 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:05:48 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:04:37 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:04:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-06 14:04:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:03:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.052 |  |
| 2026-06-06 14:03:22 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.050 |  |
| 2026-06-06 14:03:13 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.223 |  |
| 2026-06-06 14:03:13 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.031 |  |
| 2026-06-06 14:03:10 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:02:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:39 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:32 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-06 14:02:20 | Dunamale (Aththanagalu Oya) | 3.15 | 🟢 Normal | -0.033 |  |
| 2026-06-06 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:12 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:11 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-06-06 14:01:55 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:01:28 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:01:22 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-06 14:01:14 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:01:06 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:00:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-06 14:00:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 14:04:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-06 14:02:32 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-06 14:07:24 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 14:13:27 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-06 14:07:20 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 13:04:19 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 14:01:55 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:04:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:39 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:14:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:12:12 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:04:37 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:03:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:07:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:00:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:12 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:09:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:01:28 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:06:02 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:06:45 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:05:50 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-06-06 14:06:21 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:03:10 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:05:48 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:01:14 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.010 |  |
| 2026-06-06 14:00:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-06 14:01:22 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-06 14:12:20 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-06-06 14:03:13 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.031 |  |
| 2026-06-06 14:02:20 | Dunamale (Aththanagalu Oya) | 3.15 | 🟢 Normal | -0.033 |  |
| 2026-06-06 14:09:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.038 |  |
| 2026-06-06 14:02:11 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-06-06 14:03:22 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.050 |  |
| 2026-06-06 14:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.052 |  |
| 2026-06-06 14:03:13 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.223 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)