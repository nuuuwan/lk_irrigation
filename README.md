# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_13:25:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,983 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 13:25:01 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:24:46 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-18 13:17:21 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:16:15 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:08:14 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:07:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:07:53 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:07:53 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 13:07:49 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 13:06:37 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:45 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:31 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-18 13:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:05:21 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:05:21 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:13 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.100 |  |
| 2026-01-18 13:05:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.058 |  |
| 2026-01-18 13:04:48 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:04:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:04:18 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:04:00 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:03:51 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:03:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-01-18 13:03:14 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:02:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:53 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-18 13:02:34 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:28 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-01-18 13:01:39 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:33 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:31 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:00:49 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:41 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:40 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.227 |  |
| 2026-01-18 13:00:31 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:29 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.082 |  |
| 2026-01-18 12:53:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.082 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 13:02:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-18 13:05:31 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-18 13:24:46 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-18 13:04:48 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:03:51 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 13:07:49 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 13:07:53 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 13:01:39 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:41 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:16:15 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:49 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:21 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:31 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:00:31 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:28 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:17:21 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:25:01 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:01:33 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:02:53 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:06:37 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:45 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:07:53 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:05:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 13:07:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:04:18 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:04:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:03:14 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 13:03:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-01-18 13:01:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-01-18 13:05:21 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:08:14 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:04:00 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-01-18 13:05:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.058 |  |
| 2026-01-18 13:00:29 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.082 |  |
| 2026-01-18 13:05:13 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.100 |  |
| 2026-01-18 13:00:40 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)