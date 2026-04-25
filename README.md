# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_12:12:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 12:12:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:11:15 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.035 |  |
| 2026-04-25 12:09:54 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-04-25 12:09:28 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:09:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:08:25 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:07:56 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -2.233 |  |
| 2026-04-25 12:07:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:06:33 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:06:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-25 12:05:51 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-04-25 12:05:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 12:05:23 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.081 |  |
| 2026-04-25 12:05:22 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:05:07 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:05:06 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:04:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:03:40 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-25 12:03:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.063 |  |
| 2026-04-25 12:03:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-04-25 12:03:04 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:02:59 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:02:39 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:02:17 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:02:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:59 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:58 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:58 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-04-25 12:01:54 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:34 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.022 |  |
| 2026-04-25 12:01:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:02 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-25 12:00:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:00:16 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.020 |  |
| 2026-04-25 12:00:16 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 12:00:16 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 12:01:59 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:58 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:05:07 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:09:28 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:08:25 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:04:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:54 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:02:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:00:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:01:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:09:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 12:12:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:08:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 12:09:54 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-04-25 12:07:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:05:22 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:03:40 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:06:33 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:02:17 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:02:59 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-25 12:03:27 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-04-25 12:01:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-25 12:05:51 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-04-25 12:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-25 12:00:16 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.020 |  |
| 2026-04-25 12:06:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-25 12:01:58 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-04-25 12:01:34 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.022 |  |
| 2026-04-25 12:02:39 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:03:04 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-04-25 12:05:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 12:11:15 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.035 |  |
| 2026-04-25 12:03:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.063 |  |
| 2026-04-25 12:05:23 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.081 |  |
| 2026-04-25 12:07:56 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -2.233 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)