# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_02:40:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 02:40:09 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:39:53 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:16:55 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-11 02:15:52 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 02:13:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:13:04 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:51 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:33 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:33 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-06-11 02:06:17 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 02:05:54 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-11 02:05:46 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:05:29 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-11 02:04:24 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-11 02:04:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:04:15 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:48 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-06-11 02:03:42 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:38 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.167 |  |
| 2026-06-11 02:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -2.769 |  |
| 2026-06-11 02:03:20 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:00 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -2.769 |  |
| 2026-06-11 02:02:55 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 02:02:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-11 02:01:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-11 02:01:04 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:00:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 02:05:29 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-11 02:02:55 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 02:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 02:02:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-10 23:03:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 02:15:52 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 01:26:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.004 |  |
| 2026-06-11 02:39:53 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:01:04 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:00:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:42 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:05:46 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:40:09 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:04:15 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:33 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:00 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:51 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:23 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:10:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:04:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:01:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:06:17 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:13:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:20 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:16:55 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-11 02:04:24 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:27:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-11 02:03:48 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:37:22 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.013 |  |
| 2026-06-11 02:05:54 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-11 02:06:33 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-06-11 02:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-11 02:03:38 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.167 |  |
| 2026-06-11 02:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)