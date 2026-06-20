# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_01:32:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 01:32:06 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:29:41 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -2.483 |  |
| 2026-06-21 01:29:12 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -2.483 |  |
| 2026-06-21 01:12:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:12:03 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:11:47 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-06-21 01:11:16 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-06-21 01:09:42 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:09:33 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-21 01:09:14 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:09:12 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.213 |  |
| 2026-06-21 01:09:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-06-21 01:07:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 1.059 | 🔺 Rising |
| 2026-06-21 01:07:40 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:07:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 1.059 | 🔺 Rising |
| 2026-06-21 01:05:55 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-06-21 01:05:32 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 01:04:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:23 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-21 01:04:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:11 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:07 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:03:57 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-21 01:03:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.050 |  |
| 2026-06-21 01:03:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:03:00 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:02:32 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-06-21 01:02:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-21 01:02:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:02:15 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-21 01:02:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:26 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.030 |  |
| 2026-06-21 01:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:24 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:13 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.013 |  |
| 2026-06-21 01:00:43 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 01:07:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 1.059 | 🔺 Rising |
| 2026-06-21 01:03:57 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-21 01:09:33 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-21 01:02:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-21 01:05:32 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 01:12:03 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:00:43 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:12:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:11 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:03:00 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:07:40 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:02:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:02:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:32:06 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:04:07 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:03:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:09:42 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:24 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:11:16 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-06-21 01:11:47 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-06-21 01:04:23 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-21 01:02:32 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 01:02:15 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-21 01:01:13 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.013 |  |
| 2026-06-21 01:05:55 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-06-21 01:01:26 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.030 |  |
| 2026-06-21 01:09:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-06-21 00:34:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.035 |  |
| 2026-06-21 01:03:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.050 |  |
| 2026-06-21 01:09:12 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.213 |  |
| 2026-06-21 01:29:41 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -2.483 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)