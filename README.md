# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_14:22:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 14:22:16 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-19 14:16:57 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.025 |  |
| 2026-02-19 14:16:30 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:16:12 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:11:15 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:10:48 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.060 |  |
| 2026-02-19 14:09:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:07:44 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:07:25 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:07:23 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:06:46 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-19 14:06:32 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:05:54 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:05:18 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-02-19 14:05:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:05:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.095 |  |
| 2026-02-19 14:04:10 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:59 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:03:53 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:27 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:25 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:49 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 14:02:32 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:31 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:18 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:02:11 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-02-19 14:02:03 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 14:01:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:01:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-19 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-19 14:01:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-02-19 14:01:22 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:00:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:00:14 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:00:09 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 14:01:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-19 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-19 14:02:11 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-02-19 14:22:16 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-19 14:02:03 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 14:02:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 14:02:49 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:11:15 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:00:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:18 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:05:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:07:23 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:31 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:02:32 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:16:12 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:27 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:16:30 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:25 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:53 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:04:10 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:09:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:59 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:06:32 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:07:25 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:03:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:01:22 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 14:06:46 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-19 14:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:03:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:01:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:00:14 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:05:54 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-19 14:01:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-02-19 14:05:18 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-02-19 14:16:57 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.025 |  |
| 2026-02-19 14:00:09 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.046 |  |
| 2026-02-19 14:10:48 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.060 |  |
| 2026-02-19 14:05:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)