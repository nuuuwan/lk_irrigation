# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_03:21:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,203 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 03:21:32 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.008 |  |
| 2026-06-10 03:18:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-06-10 03:12:02 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:12:00 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:10:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-06-10 03:06:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:06:04 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.069 |  |
| 2026-06-10 03:05:26 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-06-10 03:05:15 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:05:15 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-10 03:04:47 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:04:39 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.058 |  |
| 2026-06-10 03:03:57 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:10 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-06-10 03:03:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-10 03:03:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:56 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:56 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-06-10 03:02:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:52 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.110 |  |
| 2026-06-10 03:02:34 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.034 |  |
| 2026-06-10 03:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:07 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 03:02:06 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.023 |  |
| 2026-06-10 03:01:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:00:44 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:59:08 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:54:22 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 03:02:07 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 03:02:06 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:01:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:04:47 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-10 00:05:02 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:12:02 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:05:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:56 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:57 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:06:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:05:15 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:02:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:01:09 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:00:44 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:21:32 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.008 |  |
| 2026-06-10 03:18:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-06-10 00:07:58 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-10 03:03:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-10 02:07:47 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-06-10 03:05:15 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:03:39 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 03:05:26 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-06-10 02:08:45 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-06-10 03:02:56 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-06-10 03:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.023 |  |
| 2026-06-10 03:10:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-10 03:02:34 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.034 |  |
| 2026-06-10 03:04:39 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.058 |  |
| 2026-06-10 03:06:04 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.069 |  |
| 2026-06-10 03:03:10 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-06-10 03:02:52 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)