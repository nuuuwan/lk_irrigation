# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_20:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,049 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 20:11:52 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.018 |  |
| 2026-06-27 20:08:29 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:08:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:07:24 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:07:13 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-27 20:05:57 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:05:40 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-27 20:05:39 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-27 20:04:41 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:04:27 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.051 |  |
| 2026-06-27 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-06-27 20:03:27 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:03:24 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 20:03:24 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:03:23 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:03:19 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-06-27 20:03:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.098 |  |
| 2026-06-27 20:03:11 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:03:08 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:53 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:02:47 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 20:02:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-06-27 20:02:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:26 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-06-27 20:02:25 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:02:07 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:04 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:01:32 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.056 |  |
| 2026-06-27 20:01:12 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:00:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:00:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 20:05:40 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-27 20:07:13 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-27 20:02:47 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 20:03:24 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:00:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:08:29 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 19:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:12 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:07:24 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:03:23 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:08:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:03:08 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:05:57 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:04:41 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:02:07 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 20:03:24 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:03:11 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:02:25 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:02:53 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:02:04 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:03:27 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-27 20:00:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-06-27 20:03:19 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-06-27 20:11:52 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.018 |  |
| 2026-06-27 20:02:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-06-27 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-06-27 20:04:27 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.051 |  |
| 2026-06-27 20:01:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.056 |  |
| 2026-06-27 20:02:26 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-06-27 20:03:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)