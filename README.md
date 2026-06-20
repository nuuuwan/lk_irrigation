# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_10:32:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 10:32:42 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:18:06 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.017 |  |
| 2026-06-20 10:12:38 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.027 |  |
| 2026-06-20 10:12:30 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:11:45 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:07:26 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.040 |  |
| 2026-06-20 10:06:58 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:06:58 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-20 10:05:55 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:05:13 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:56 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:50 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:42 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:04:37 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-20 10:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:04:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-06-20 10:03:45 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-06-20 10:03:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:03:22 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:03:06 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:48 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:38 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-06-20 10:02:00 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:00 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-06-20 10:01:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:51 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-06-20 10:01:46 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.097 |  |
| 2026-06-20 10:01:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:32 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:01:26 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.020 |  |
| 2026-06-20 10:01:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-06-20 10:01:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 10:04:37 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-20 10:06:58 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-20 10:01:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 10:05:13 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:11:45 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:03:06 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:12:30 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:03:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:00 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:06:58 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:38 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:56 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:05:55 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:02:48 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:50 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:32:42 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:51 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:01:46 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 10:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:03:22 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:01:32 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:04:42 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-20 10:18:06 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.017 |  |
| 2026-06-20 10:01:26 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.020 |  |
| 2026-06-20 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:00:54 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.022 |  |
| 2026-06-20 10:12:38 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.027 |  |
| 2026-06-20 10:02:00 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-06-20 10:01:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-06-20 10:01:51 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-06-20 10:07:26 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.040 |  |
| 2026-06-20 10:04:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-06-20 10:03:45 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-06-20 10:01:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)