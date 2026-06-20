# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_05:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,082 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 05:09:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-21 05:06:53 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.010 |  |
| 2026-06-21 05:06:35 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:06:20 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 05:06:02 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:05:09 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:05:08 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:04:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:03:52 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:03:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 05:03:23 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-06-21 05:03:00 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-21 05:02:52 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 05:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2026-06-21 05:02:37 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:02:37 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:02:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:51 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-21 05:01:49 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.069 |  |
| 2026-06-21 05:01:48 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:01 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:00:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-21 04:48:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-06-21 04:40:19 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:37:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-21 04:34:37 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-06-21 04:29:09 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 04:28:27 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:23:43 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 05:00:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-21 03:02:20 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-21 05:03:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 05:09:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-21 05:01:51 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-21 04:01:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 05:02:52 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 05:06:20 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 05:01:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:02:37 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:04:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:05:11 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:05:09 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:02:37 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:03:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:02:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:06:14 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:01 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:03:52 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:03:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:06:35 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 05:01:48 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:48:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-06-21 05:06:53 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:04:52 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-21 04:02:26 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-21 05:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2026-06-21 05:03:23 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-06-21 04:10:18 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.025 |  |
| 2026-06-21 04:11:51 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-06-21 05:03:00 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-21 04:16:11 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.055 |  |
| 2026-06-21 05:01:49 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)