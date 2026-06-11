# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_19:15:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 19:15:57 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-11 19:14:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:13:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:11:28 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-11 19:10:29 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-11 19:09:58 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-06-11 19:09:08 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-06-11 19:08:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 19:08:20 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-06-11 19:08:00 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-06-11 19:06:59 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:06:55 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 19:05:27 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 19:05:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:04:57 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:04:31 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-11 19:04:09 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 19:04:02 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-11 19:03:59 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-11 19:03:43 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-11 19:03:26 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:03:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:58 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 19:02:54 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 19:02:33 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:18 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 19:02:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:16 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 19:02:03 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-11 19:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-06-11 19:01:57 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:01:51 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:01:37 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 19:01:27 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-11 19:00:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 19:09:08 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-06-11 19:03:59 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-11 19:01:27 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-11 19:10:29 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-11 19:15:57 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-11 19:04:02 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-11 19:03:43 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-11 19:02:03 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-11 19:02:54 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 19:02:16 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 18:02:46 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-11 19:11:28 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-11 19:01:37 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 19:02:18 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 19:08:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 19:06:55 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 19:04:09 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 19:02:58 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 19:04:31 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-11 19:05:27 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 19:02:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:00:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:01:51 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:01:57 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:06:59 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:03:48 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:05:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:03:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:03:26 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:02:33 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:14:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 19:09:58 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-06-11 19:08:00 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-06-11 19:08:20 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-11 19:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)