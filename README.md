# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_01:25:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,144 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 01:25:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:16:02 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.017 |  |
| 2026-06-10 01:09:41 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:09:05 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-10 01:08:55 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:08:13 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:07:17 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-10 01:06:37 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:06:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 4.312 | 🔺 Rising |
| 2026-06-10 01:06:15 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.031 |  |
| 2026-06-10 01:06:13 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.020 |  |
| 2026-06-10 01:05:39 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:05:10 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-10 01:04:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:04:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-06-10 01:04:18 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.188 |  |
| 2026-06-10 01:03:39 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 01:03:37 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:03:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 01:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.060 |  |
| 2026-06-10 01:03:10 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:03:04 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 01:03:00 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:02:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:02:34 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:02:30 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:01:39 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:00:42 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:00:30 | Wellawaya (Kirindi Oya) | 0.10 | 🟢 Normal | 4.312 | 🔺 Rising |
| 2026-06-10 00:35:55 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 01:06:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 4.312 | 🔺 Rising |
| 2026-06-10 00:04:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-06-10 01:09:05 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-10 01:05:10 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-10 01:03:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 01:03:04 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 01:04:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:29 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 00:05:02 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:00:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:02:30 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:03:10 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:09:41 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:02:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:02:34 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:08:13 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:03:37 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:00:42 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:05:39 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-10 00:03:44 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:01:39 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:25:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 01:07:17 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-10 00:07:58 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:08:55 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:03:00 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:06:37 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-10 00:07:00 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:03:39 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 01:16:02 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.017 |  |
| 2026-06-10 01:06:13 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.020 |  |
| 2026-06-10 01:06:15 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.031 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-10 01:04:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-06-10 01:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.060 |  |
| 2026-06-10 01:04:18 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)