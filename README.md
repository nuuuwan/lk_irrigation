# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_14:22:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 14:22:34 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:13:44 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-06-20 14:09:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:08:59 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:08:55 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:07:44 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.059 |  |
| 2026-06-20 14:06:08 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-20 14:05:15 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:05:12 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.051 |  |
| 2026-06-20 14:04:45 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:04:35 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:04:19 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:04:19 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-06-20 14:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.078 |  |
| 2026-06-20 14:03:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:28 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:18 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:14 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:02:55 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:02:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 14:02:29 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:02:18 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:17 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:08 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 14:02:01 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.021 |  |
| 2026-06-20 14:01:58 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-20 14:01:58 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-06-20 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:01:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:01:12 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-06-20 14:01:08 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:00:38 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:00:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.119 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 14:01:58 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-06-20 14:01:58 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-20 14:00:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-20 14:06:08 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-20 14:02:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 14:02:08 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 14:03:28 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:04:35 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:09:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:12:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:08:55 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:01:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:05:15 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:18 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:04:19 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:22:34 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:03:18 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:02:17 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 14:13:44 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-06-20 14:04:45 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:02:55 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:01:08 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:07:44 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:00:38 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 14:01:12 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-06-20 14:04:19 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-06-20 14:02:29 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:08:59 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:03:14 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.020 |  |
| 2026-06-20 14:02:01 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.021 |  |
| 2026-06-20 14:05:12 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.051 |  |
| 2026-06-20 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.059 |  |
| 2026-06-20 14:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)