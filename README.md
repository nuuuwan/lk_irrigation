# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_04:19:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,648 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 04:19:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-06-25 04:15:22 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.016 |  |
| 2026-06-25 04:15:20 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.016 |  |
| 2026-06-25 04:12:12 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-06-25 04:12:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-25 04:07:11 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:07:10 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:07:09 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:07:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:06:17 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 04:05:50 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:05:21 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:05:19 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.022 |  |
| 2026-06-25 04:05:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:51 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:48 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:32 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-25 04:04:26 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:03:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-06-25 04:03:02 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-06-25 04:03:01 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:02:59 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:02:58 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.008 |  |
| 2026-06-25 04:02:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.258 |  |
| 2026-06-25 04:02:25 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:02:12 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.014 |  |
| 2026-06-25 04:01:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:01:41 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 04:01:32 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 04:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 04:01:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 04:04:32 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-25 04:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 04:01:32 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 04:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 04:01:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 04:06:17 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 03:01:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-25 03:00:40 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:02:59 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:07:11 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:05:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:05:21 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:48 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:26 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:03:01 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:01:41 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:02:58 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.008 |  |
| 2026-06-25 04:19:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-06-25 04:12:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-25 04:12:12 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-06-25 04:05:50 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:02:25 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:01:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:03:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-06-25 04:02:12 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.014 |  |
| 2026-06-25 04:15:22 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.016 |  |
| 2026-06-25 04:15:20 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.016 |  |
| 2026-06-25 04:05:19 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.022 |  |
| 2026-06-25 03:05:21 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-06-25 04:03:02 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-06-25 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.056 |  |
| 2026-06-25 03:05:52 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.082 |  |
| 2026-06-25 02:02:50 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.255 |  |
| 2026-06-25 04:02:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.258 |  |
| 2026-06-25 03:08:31 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -5.684 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)