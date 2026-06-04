# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_23:24:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 23:24:57 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:39 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:17:16 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:09:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:07:59 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-06-04 23:07:43 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-04 23:06:28 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-06-04 23:06:04 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:06:01 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.052 |  |
| 2026-06-04 23:05:52 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 23:05:20 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.071 |  |
| 2026-06-04 23:05:07 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.124 |  |
| 2026-06-04 23:05:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:04:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 23:04:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:04:18 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-04 23:03:55 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-04 23:03:53 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-04 23:03:52 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.169 |  |
| 2026-06-04 23:03:14 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:03:13 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 23:03:13 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:02:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 23:02:11 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-04 23:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 23:02:10 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-04 23:02:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-04 23:01:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:13 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-04 23:01:09 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 22:12:21 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-04 23:02:11 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-04 23:07:43 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-04 23:03:53 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-04 23:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 23:03:13 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 23:04:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 23:04:18 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-04 23:05:52 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 23:02:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:04:19 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 23:03:13 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:02:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:39 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:17:16 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:24:57 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:09 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:05:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:09:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:04:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:03:14 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:06:28 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-06-04 23:03:55 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-04 23:01:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-04 23:01:13 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-04 23:02:10 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-04 23:07:59 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-06-04 22:10:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.037 |  |
| 2026-06-04 23:06:01 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.052 |  |
| 2026-06-04 23:05:20 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.071 |  |
| 2026-06-04 23:05:07 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.124 |  |
| 2026-06-04 23:03:52 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)