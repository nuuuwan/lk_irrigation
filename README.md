# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_23:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 23:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 23:07:58 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-28 23:06:46 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-28 23:06:03 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:29 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-28 23:05:13 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 23:04:54 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:04:48 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-28 23:04:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:49 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:38 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:27 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 23:03:03 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:02:36 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:02:36 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:02:35 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:02:33 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 23:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:02:05 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 23:01:56 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-06-28 23:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:01:17 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:01:09 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-28 23:00:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:00:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:00:42 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 22:56:29 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 22:54:29 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 23:05:29 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-28 23:06:46 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-28 23:04:48 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-28 23:07:58 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-28 21:06:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-28 23:02:33 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 23:05:13 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 23:02:05 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 23:03:27 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 23:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 22:10:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:00:42 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:06:03 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-28 21:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:00:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:38 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:49 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:04:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-28 21:00:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 22:08:35 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:04:54 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:02:36 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:03:03 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:02:36 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:01:17 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:00:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:02:35 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-28 22:10:12 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 23:01:56 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-06-28 23:01:09 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-28 22:03:05 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-06-28 22:04:34 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)