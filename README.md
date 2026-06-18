# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_23:23:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,095 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 23:23:33 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:09:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:09:02 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:08:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:08:05 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-18 23:07:55 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:07:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-06-18 23:06:47 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.018 |  |
| 2026-06-18 23:06:42 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 23:04:45 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.014 |  |
| 2026-06-18 23:04:23 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:04:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 23:04:09 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:04:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 23:03:59 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 23:03:48 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:49 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-06-18 23:02:18 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:12 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 23:02:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:49 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.032 |  |
| 2026-06-18 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-18 23:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:32 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2026-06-18 23:01:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:28 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:28 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:12 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:09 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:00:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 23:03:59 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 23:04:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 23:04:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 23:02:12 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 23:06:42 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 23:02:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:09 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:00:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:40 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:09:02 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:08:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:07:55 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:04:09 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:28 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:18 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:02:49 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:28 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:03:48 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:04:23 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:23:33 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:09:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:12 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-18 23:08:05 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-18 23:04:45 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.014 |  |
| 2026-06-18 23:06:47 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.018 |  |
| 2026-06-18 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-06-18 23:01:32 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2026-06-18 23:07:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-06-18 23:01:49 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.032 |  |
| 2026-06-18 22:04:57 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-18 22:07:15 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.051 |  |
| 2026-06-18 22:14:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)